# Python Learning IDE for Kids

A fully client-side Python coding environment designed for middle school students (11+) to learn Python programming. Runs entirely in the browser using Pyodide (WebAssembly) and can be hosted on GitHub Pages.

![Python IDE Screenshot](screenshot.png)

## Features

### Core Functionality
- **Monaco Editor** - VS Code's editor with Python syntax highlighting, auto-indentation, and bracket matching
- **Pyodide Runtime** - Full Python 3.11+ with standard library running in browser via WebAssembly
- **No Server Required** - Works entirely client-side, perfect for GitHub Pages hosting
- **Zero Build Step** - Single HTML file with all dependencies loaded via CDN

### File Management
- Multi-file support with tabbed interface
- Create, rename, and delete files
- Files persist in localStorage across sessions
- Auto-save on every keystroke

### Python Execution
- Run code directly in browser
- Real-time console output
- Kid-friendly error messages
- Loading indicator during Pyodide initialization (~5-10 seconds first load)

### Turtle Graphics
- Custom turtle implementation for browser
- Step-by-step drawing animation
- HTML5 Canvas rendering
- Supports: `forward()`, `backward()`, `left()`, `right()`, `penup()`, `pendown()`, `color()`, `width()`, `circle()`, `goto()`, `home()`, `dot()`

### Code Sharing
- Share active file via compressed URL
- One-click copy to clipboard
- Load code from shared links

### UI/UX
- **Dark/Light theme** toggle with persistent preference
- **Five starter templates**:
  1. Hello World - Basic print and input
  2. Calculator - Math operations and conditionals
  3. Turtle Spiral - Introduction to graphics
  4. Guessing Game - Random numbers and loops
  5. Mad Libs - String manipulation
- **Responsive design** for desktop and tablet
- **Resizable** output panel
- **Keyboard shortcuts** (Ctrl+Enter to run)

## Quick Start

### Local Development
1. Clone or download this repository
2. Open `index.html` in any modern browser
3. That's it! No build step required

### GitHub Pages Deployment
1. Fork or push this repository to GitHub
2. Go to repository **Settings** → **Pages**
3. Select **Deploy from a branch**
4. Choose **main** (or **master**) branch and **/(root)** folder
5. Click **Save**
6. Your IDE will be available at `https://yourusername.github.io/python-learning-ide/`

## Usage

### Running Code
- Click the **Run** button or press **Ctrl+Enter** (Cmd+Enter on Mac)
- Output appears in the Console tab
- Turtle graphics appear in the Turtle tab

### Creating Files
- Click **+ New** in the Explorer sidebar
- Double-click a filename to rename
- Click the **×** on a tab to delete

### Sharing Code
- Click **🔗 Share** to copy a link with your code
- Anyone with the link can load your code instantly

### Switching Themes
- Click **🌓 Theme** to toggle between dark and light modes
- Your preference is saved automatically

### Using Templates
- Click **📋 Templates** to see available examples
- Select any template to load it into the current file

## Browser Compatibility

- Chrome 90+
- Firefox 90+
- Safari 14+
- Edge 90+

Requires WebAssembly support (all modern browsers).

## File Structure

```
.
├── index.html          # Main application (single file)
├── PLAN.md             # Implementation plan
├── README.md           # This file
└── examples/           # Starter templates
    ├── hello_world.py
    ├── calculator.py
    ├── turtle_spiral.py
    ├── guessing_game.py
    └── mad_libs.py
```

## Technology Stack

### CDN Dependencies
- **Monaco Editor** - `https://cdn.jsdelivr.net/npm/monaco-editor@0.44.0/`
- **Pyodide** - `https://cdn.jsdelivr.net/pyodide/v0.25.0/`
- **LZ-String** - `https://cdn.jsdelivr.net/npm/lz-string@1.4.4/`

### Browser APIs Used
- WebAssembly
- LocalStorage
- Canvas 2D Context
- Clipboard API

## Customization

### Adding New Templates
Edit the `templates` object in `index.html`:

```javascript
const templates = {
    // ... existing templates
    my_template: `print("Your code here")`
};
```

Then add to the dropdown menu in the HTML.

### Changing Default Files
Modify the default files in the `loadFiles()` function:

```javascript
state.files = {
    'main.py': { content: templates.hello },
    'lesson1.py': { content: '# Your default content' }
};
```

### Styling
CSS variables are defined at the top of the `<style>` section. Modify these to change colors:

```css
:root {
    --bg-primary: #1e1e1e;
    --bg-secondary: #252526;
    --accent: #007acc;
    /* ... */
}
```

## Limitations

- **Initial Load**: ~10MB download for Pyodide (cached after first load)
- **File System**: No real file system access (all files stored in localStorage)
- **Package Installation**: Limited to packages included with Pyodide or pure Python packages via micropip
- **Network**: Requires internet connection to load CDNs (can be made offline with local assets)

## Educational Use Cases

- **Classroom Teaching**: Students can code along on any device with a browser
- **Homework Assignments**: Teachers share starter code via URLs
- **Self-Paced Learning**: Templates provide structured progression
- **Summer Camps**: No setup required, works on Chromebooks
- **Coding Clubs**: Easy to deploy and share

## Troubleshooting

### "Loading Python environment..." stays too long
- Check internet connection (Pyodide needs to download)
- First load takes 5-10 seconds, subsequent loads use cache

### Code doesn't run
- Check browser console for errors
- Ensure JavaScript is enabled
- Try refreshing the page

### Files not persisting
- Check if localStorage is enabled in browser
- Private/incognito mode may clear storage

### Turtle graphics not showing
- Make sure `import turtle` is in your code
- Click the "Turtle" tab in the output panel
- Check console for error messages

## Contributing

This is an educational project. Feel free to:
- Fork and customize for your needs
- Submit improvements via pull requests
- Report issues or suggest features
- Add more templates for beginners

## License

MIT License - Free for educational and personal use

## Acknowledgments

- [Pyodide](https://pyodide.org/) - Python in the browser
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) - VS Code's editor
- [LZ-String](https://github.com/pieroxy/lz-string/) - URL compression

## Support

For questions or issues:
1. Check the [troubleshooting](#troubleshooting) section
2. Open an issue on GitHub
3. Review the [Pyodide documentation](https://pyodide.org/en/stable/)

---

**Happy Coding! 🐍✨**
