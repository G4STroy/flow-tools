// src/App.js
import React, { useEffect } from 'react';

function App() {
  useEffect(() => {
    // Setting up listeners
    const removeConversionCompleteListener = window.electron.receive('conversion-complete', (savedFilePath) => {
      console.log(`File converted and saved to ${savedFilePath}`);
    });
  
    const removeConversionErrorListener = window.electron.receive('conversion-error', (error) => {
      console.error(`Conversion error: ${error}`);
    });
  
    // Cleanup function to remove listeners
    return () => {
      removeConversionCompleteListener();
      removeConversionErrorListener();
    };
  }, []);
  
  // Function to send IPC message to Electron's main process for file conversion
  const handleConversion = () => {
    if (window.electron) {
      window.electron.send('convert-file');
    } else {
      console.error("Electron's IPC is not available");
    }
  };

  // Function to send IPC message to Electron's main process for template downloading
  const handleDownloadTemplate = () => {
    if (window.electron) {
      window.electron.send('download-template');
    } else {
      console.error("Electron's IPC is not available");
    }
  };

  return (
    <div>
      <h1>Hours to Days Converter</h1>
      <button onClick={handleConversion}>Convert File</button>
      <button onClick={handleDownloadTemplate}>Download Template</button>
    </div>
  );
}

export default App;
