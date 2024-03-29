const { contextBridge, ipcRenderer } = require('electron');

// Defining valid channels for send and receive to enhance security.
const validSendChannels = ["convert-file", "download-template"];
const validReceiveChannels = ["conversion-complete", "conversion-error", "template-download-complete", "template-download-canceled"];

contextBridge.exposeInMainWorld('electron', {
  send: (channel, data) => {
    if (validSendChannels.includes(channel)) {
      ipcRenderer.send(channel, data);
    }
  },
  receive: (channel, func) => {
    if (validReceiveChannels.includes(channel)) {
      // Using a more specific method for adding event listeners.
      const listener = (event, ...args) => func(...args);
      ipcRenderer.on(channel, listener);

      // Return a cleanup function to remove the listener when the component unmounts or no longer needs it.
      return () => {
        ipcRenderer.removeListener(channel, listener);
      };
    }
  },
  removeAllListeners: (channel) => {
    if (validSendChannels.includes(channel) || validReceiveChannels.includes(channel)) {
      ipcRenderer.removeAllListeners(channel);
    }
  }
});
