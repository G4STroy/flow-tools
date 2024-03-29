const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');

// Define the path to your template
const templatePath = path.join(__dirname, 'Hours To Days Converter', 'HoursConvertTemplate.xlsx');

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            nodeIntegration: false,
            sandbox: false // This can be set to false unless you have specific security requirements
        },
    });

    const isDev = !app.isPackaged;
    const startUrl = isDev ? 'http://localhost:3000' : `file://${path.join(__dirname, 'build', 'index.html')}`;
    mainWindow.loadURL(startUrl);

    //if (isDev) {
     //   mainWindow.webContents.openDevTools();
    //}
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});

// IPC handler for file conversion
ipcMain.on('convert-file', async (event) => {
    const pythonScriptPath = path.join(__dirname, 'Hours To Days Converter', 'converthourstodays.py');

    const { canceled, filePaths } = await dialog.showOpenDialog({
        title: 'Select a File for Conversion',
        properties: ['openFile'],
        filters: [
            { name: 'Excel Files', extensions: ['xlsx'] }
        ]
    });

    if (canceled || filePaths.length === 0) {
        event.reply('conversion-canceled');
        return;
    }

    const selectedFilePath = filePaths[0];
    const { filePath: userChosenPath } = await dialog.showSaveDialog({
        title: 'Save Converted File',
        buttonLabel: 'Save',
        defaultPath: path.join(app.getPath('downloads'), 'ConvertedHours.xlsx'),
        filters: [
            { name: 'Excel Files', extensions: ['xlsx'] }
        ]
    });

    if (!userChosenPath) {
        event.reply('conversion-canceled');
        return;
    }

    fs.mkdirSync(path.dirname(userChosenPath), { recursive: true });
    const pythonProcess = spawn('python', [pythonScriptPath, selectedFilePath, userChosenPath]);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        event.reply('conversion-error', data.toString());
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        if (code === 0) {
            event.reply('conversion-complete', userChosenPath);
        } else {
            event.reply('conversion-error', 'Conversion failed');
        }
    });
});

// IPC handler for template downloading
ipcMain.on('download-template', async (event) => {
    // Trigger a save dialog for the user to save the template
    const { filePath: userChosenPath } = await dialog.showSaveDialog({
        title: 'Save Template File',
        buttonLabel: 'Save',
        defaultPath: path.join(app.getPath('downloads'), 'HoursConvertTemplate.xlsx'),
        filters: [{ name: 'Excel Files', extensions: ['xlsx'] }],
    });

    if (!userChosenPath) {
        event.reply('template-download-canceled');
        return;
    }

    // Copy the template file to the user's chosen path
    fs.copyFileSync(templatePath, userChosenPath);
    event.reply('template-download-complete', userChosenPath);
});
