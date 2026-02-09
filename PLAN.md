# Python Learning IDE for Kids (11+)

A client-side Python coding environment designed for middle school students to learn Python programming.

## Overview

A fully client-side web application that provides a complete Python development environment running entirely in the browser using Pyodide (WebAssembly). Hosted on GitHub Pages with zero server requirements.

## Technology Stack

### Core Technologies
- **Monaco Editor** - VS Code's editor component via CDN (syntax highlighting, IntelliSense)
- **Pyodide v0.25+** - Python runtime compiled to WebAssembly
- **LZ-String** - Compression library for URL sharing
- **Vanilla JavaScript** - No build tools or frameworks

### CDNs Used
- Monaco Editor: jsDelivr
- Pyodide: jsDelivr
- LZ-String: jsDelivr

## Features

### 1. Multi-File Support
- Tabbed interface for managing multiple Python files
- Default files: `main.py`, `helpers.py`, `turtle_example.py`
- CRUD operations (Create, Rename, Delete files)
- Files persist in localStorage across sessions
- Auto-save on every keystroke (debounced)

### 2. Code Editor
- Monaco Editor with Python mode
- Line numbers
- Syntax highlighting
- Auto-indentation
- Bracket matching
- Dark/Light theme toggle

### 3. Python Execution
- Run Python code in browser using Pyodide
- Real-time console output
- Error handling with kid-friendly messages
- Loading indicator while Pyodide initializes (~5-10 seconds first load)

### 4. Turtle Graphics
- Custom turtle module implementation
- Step-by-step animation for educational value
- HTML5 Canvas rendering
- Supported commands: forward(), backward(), left(), right(), penup(), pendown(), color(), width(), speed(), circle()

### 5. Code Sharing
- Share active file via URL (compressed with LZ-String)
- Copy-to-clipboard button
- Load code from URL on page open

### 6. Starter Templates
Five beginner-friendly examples:
1. Hello World - Basic print statements
2. Calculator - Input and math operations
3. Turtle Spiral - Graphics introduction
4. Guessing Game - Random numbers and loops
5. Mad Libs - String manipulation

### 7. UI/UX
- Responsive design (desktop + tablet)
- Loading spinner for Pyodide initialization
- Success feedback (subtle animations)
- Kid-friendly error messages
- File explorer sidebar
- Output console panel
- Turtle graphics canvas (toggle with console)

## Project Structure

```
repo/
├── index.html          # Main application (single file)
├── PLAN.md             # This document
├── README.md           # User documentation
└── examples/           # Starter code templates
    ├── hello_world.py
    ├── calculator.py
    ├── turtle_spiral.py
    ├── guessing_game.py
    └── mad_libs.py
```

## Implementation Details

### State Management
```javascript
{
  files: {
    'main.py': { content: '...', isActive: true },
    'helpers.py': { content: '...', isActive: false }
  },
  activeFile: 'main.py',
  theme: 'dark',
  turtleSpeed: 5 // 1-10
}
```

### Pyodide Integration
- Load Pyodide from CDN
- Initialize with required packages (micropip, turtle replacement)
- Redirect stdout/stderr to custom console
- Intercept turtle commands for canvas rendering

### URL Sharing Format
```
https://user.github.io/python-learning-ide/#lz-string-compressed-code
```

### localStorage Keys
- `pyide_files`: JSON string of all files
- `pyide_theme`: 'dark' or 'light'

## Browser Compatibility
- Chrome 90+
- Firefox 90+
- Safari 14+
- Edge 90+

## Deployment

### GitHub Pages Setup
1. Push code to repository
2. Go to Settings > Pages
3. Select source branch (main or master)
4. Site will be available at `https://username.github.io/repo-name/`

### No Build Step Required
- All dependencies loaded via CDN
- Single HTML file contains all logic
- Examples loaded from separate files (optional, can embed)

## Future Enhancements
- Export files as .py downloads
- Import .py files
- Multiple turtle instances
- Package installation UI (micropip)
- Collaborative editing (WebRTC)

## License
MIT License - Free for educational use
