# Projects Folder - Quick Guide

## Folder Structure
```
/projects/
├── index.html                        (Main portfolio page - UPDATE THIS)
├── _template.html                    (Copy this to create new projects)
├── _INSTRUCTIONS.md                  (This file)
├── example-network-analysis.html     (Full example showing capabilities)
├── your-project-1.html               (Your actual projects go here)
└── your-project-2.html
```

## Adding a New Project (3 Steps)

### Step 1: Create the Project Page
1. **Copy** `_template.html`
2. **Rename** it to something descriptive: `network-analysis-project.html`
3. **Edit** the marked sections:
   - Title and meta description (top of file)
   - Project title in header
   - Metadata (date, duration, category)
   - Tags
   - Links (GitHub, report, etc.)
   - All content sections

### Step 2: Add to Portfolio Grid
1. Open `/projects/index.html`
2. Find the commented `<!-- PROJECT CARD TEMPLATE -->` section (around line 250)
3. **Copy** that entire block
4. **Paste** it above the existing example projects
5. **Edit** the card content:
   ```html
   <div class="project-card" data-category="network">  <!-- Change category -->
       <div class="project-image network">            <!-- Change class/icon -->
           <i class="fas fa-project-diagram"></i>
           <div class="project-status status-complete">Complete</div>
       </div>
       <div class="project-content">
           <h3>Your Project Title</h3>              <!-- Edit -->
           <div class="project-date">Month Year</div>
           <p class="project-description">
               Your description here                 <!-- Edit -->
           </p>
           <div class="project-tags">
               <span class="tag">Python</span>       <!-- Edit tags -->
           </div>
           <div class="project-links">
               <a href="/projects/your-file.html" class="project-link">  <!-- Update link -->
                   <i class="fas fa-arrow-right"></i> View Project
               </a>
           </div>
       </div>
   </div>
   ```

### Step 3: Push to GitHub
```bash
git add projects/
git commit -m "Add new project: [Your Project Name]"
git push origin main
```

## Quick Reference

### Project Categories (for filtering)
- `network` - Network Analysis
- `abm` - Agent-Based Models
- `data` - Data Analysis
- `risk` - Risk Analysis

### Project Image Styles
```html
<div class="project-image network">    <!-- Purple gradient -->
<div class="project-image abm">        <!-- Pink/red gradient -->
<div class="project-image data">       <!-- Blue gradient -->
<div class="project-image risk">       <!-- Orange/yellow gradient -->
```

### Status Options
```html
<div class="project-status status-complete">Complete</div>
<div class="project-status status-progress">In Progress</div>
```

### Common Icons
- Network: `<i class="fas fa-project-diagram"></i>`
- Data: `<i class="fas fa-chart-line"></i>`
- ABM: `<i class="fas fa-users"></i>`
- Code: `<i class="fas fa-code"></i>`
- Database: `<i class="fas fa-database"></i>`

[See all icons at Font Awesome: https://fontawesome.com/icons]

## Tips for Project Pages

### Writing Content
- Start with a compelling overview - why should someone care?
- Be specific about methods and tools
- Include limitations - shows maturity and critical thinking
- Add future directions - demonstrates forward thinking

### Visuals
- Use placeholder images initially: `https://via.placeholder.com/800x400`
- Replace with your actual visualizations later
- Always include figure captions

### Code Blocks
- Keep code snippets short and relevant
- Focus on interesting/novel parts of your implementation
- Explain what the code does after showing it

### For Recruiters
- Highlight practical applications
- Quantify results where possible (X% improvement, Y data points analyzed)
- Show progression: problem → method → results → implications

## Need Help?

### Simple Project
Just copy `_template.html` and fill in the sections. It's mostly plain text!

### Complex/Custom Project
Tell Claude: "Create a project page for [description]" and I'll generate custom HTML with:
- Interactive visualizations
- Custom layouts
- Data tables
- Whatever you need!

### Updating the Portfolio Grid
If you're unsure, just tell me your project details and I'll give you the exact HTML to paste into `index.html`.

## Remember
- Every project = 1 new HTML file in `/projects/`
- Every project = 1 new card in `/projects/index.html`
- That's it! No database, no complex build process.

The template handles all the styling automatically. Just focus on your content!
