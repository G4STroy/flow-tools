#!/bin/bash

# Run PyInstaller
pyinstaller MCHowManyapp.spec

# Copy resources to the correct location in the app bundle
cp -R "/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/Resources/" "dist/MCHowManyapp.app/Contents/Resources/"