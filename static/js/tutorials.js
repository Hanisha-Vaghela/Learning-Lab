// Initialize the page with proper styling based on language
document.addEventListener('DOMContentLoaded', function() {
    // Detect language from page title
    const title = document.title.toLowerCase();
    let langClass = '';
    
    if (title.includes('c#')) langClass = 'csharp-tutorial';
    else if (title.includes(' c ')) langClass = 'c-tutorial';
    else if (title.includes('css')) langClass = 'css-tutorial';
    else if (title.includes('html')) langClass = 'html-tutorial';
    else if (title.includes('javascript')) langClass = 'js-tutorial';
    else if (title.includes('python')) langClass = 'python-tutorial';
    
    if (langClass) document.body.classList.add(langClass);
    
    // Activate first section
    const firstSubTopic = document.querySelector('.subtopic');
    if (firstSubTopic) {
        firstSubTopic.classList.add('active');
        const sectionId = firstSubTopic.textContent.trim().toLowerCase().replace(/[ /]/g, '-');
        const section = document.getElementById(sectionId);
        if (section) section.classList.add('active');
    }
    
    // Initialize all demos that need setup
    initializeDemos();
});

// Navigation handling
document.querySelectorAll('.topic-item').forEach(item => {
    item.addEventListener('click', function() {
        document.querySelectorAll('.topic-item').forEach(i => {
            i.classList.remove('active');
        });
        this.classList.add('active');
    });
});

document.querySelectorAll('.subtopic').forEach(item => {
    item.addEventListener('click', function(e) {
        e.stopPropagation();
        
        // Remove active class from all subtopics
        document.querySelectorAll('.subtopic').forEach(sub => {
            sub.classList.remove('active');
        });
        
        // Add active class to clicked subtopic
        this.classList.add('active');
        
        // Hide all sections
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });
        
        // Show the selected section
        const sectionId = this.textContent.trim().toLowerCase().replace(/[ /]/g, '-');
        const section = document.getElementById(sectionId);
        if (section) {
            section.classList.add('active');
            section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Function to run code in demos
function runCode(code, language, outputId) {
    try {
        // In a real implementation, this would connect to a language interpreter
        // For this demo, we'll simulate output
        const outputDiv = document.getElementById(outputId);
        
        if (outputDiv) {
            let outputText = 'Output would appear here in a real environment';
            
            // Simulate some common outputs
            if (language === 'python') {
                if (code.includes('print("Hello, World!")')) {
                    outputText = 'Hello, World!';
                }
                else if (code.includes('x=5')) {
                    outputText = '5\nHello';
                }
            }
            else if (language === 'javascript') {
                if (code.includes('console.log(')) {
                    outputText = code.match(/console\.log\(([^)]+)\)/)[1];
                }
            }
            
            outputDiv.textContent = outputText;
            outputDiv.style.display = 'block';
        }
    } catch (e) {
        console.error("Error running code:", e);
    }
}

// Special function for Python "Try it" buttons
function runPythonCode(code) {
    const outputId = code.match(/runPythonCode\('([^']+)/)[1];
    runCode(code, 'python', outputId + '-output');
}

// Initialize any demo elements that need setup
function initializeDemos() {
    // Canvas demo for HTML tutorial
    const canvas = document.getElementById('myCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = '#3498db';
        ctx.fillRect(50, 20, 100, 50);
    }
    
    // SVG demo for HTML tutorial
    const svg = document.querySelector('svg circle');
    if (svg) {
        svg.setAttribute('fill', '#3498db');
    }
    
    // Event demo for JavaScript tutorial
    const eventBtn = document.getElementById('eventBtn');
    const eventOutput = document.getElementById('eventOutput');
    if (eventBtn && eventOutput) {
        eventBtn.addEventListener('click', function(e) {
            eventOutput.innerHTML = `
                Event details:<br>
                Type: ${e.type}<br>
                Target: ${e.target.tagName}<br>
                Timestamp: ${e.timeStamp}<br>
                Coordinates: (${e.clientX}, ${e.clientY})
            `;
        });
    }
    
    // Geolocation demo for HTML tutorial
    const geoBtn = document.querySelector('button[onclick="getLocation()"]');
    if (geoBtn) {
        geoBtn.addEventListener('click', function() {
            const output = document.getElementById('demo-location');
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => {
                        output.innerHTML = 
                            `Latitude: ${position.coords.latitude}<br>
                             Longitude: ${position.coords.longitude}`;
                    },
                    error => {
                        output.textContent = "Error getting location: " + error.message;
                    }
                );
            } else {
                output.textContent = "Geolocation is not supported by this browser.";
            }
        });
    }
}

// Handle all "Try it" buttons
document.querySelectorAll('.tryit-button').forEach(button => {
    if (!button.onclick) {
        button.addEventListener('click', function() {
            const codeBlock = this.previousElementSibling;
            if (codeBlock && codeBlock.classList.contains('code-example')) {
                const code = codeBlock.textContent.trim();
                const outputId = 'output-' + Math.random().toString(36).substr(2, 5);
                
                // Create output div if it doesn't exist
                let outputDiv = this.nextElementSibling;
                if (!outputDiv || !outputDiv.classList.contains('output')) {
                    outputDiv = document.createElement('div');
                    outputDiv.className = 'output';
                    this.parentNode.insertBefore(outputDiv, this.nextSibling);
                }
                
                outputDiv.id = outputId;
                runCode(code, 'javascript', outputId);
            }
        });
    }
});