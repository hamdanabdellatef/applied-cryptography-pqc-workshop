/* Render authored Mermaid fences while keeping their source available.
 * Pinned CDN dependency; explanatory prose remains usable offline.
 */
(async function () {
  const blocks = [...document.querySelectorAll('pre > code.language-mermaid')];
  if (!blocks.length) return;
  let mermaid;
  try {
    ({ default: mermaid } = await import('https://cdn.jsdelivr.net/npm/mermaid@11.12.0/dist/mermaid.esm.min.mjs'));
    mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: 'neutral',
      fontFamily: 'Arial, sans-serif', flowchart: { htmlLabels: false },
      themeVariables: { xyChart: { plotColorPalette: '#196a83', backgroundColor: '#ffffff' } } });
  } catch (error) {
    for (const block of blocks) {
      const message = document.createElement('p');
      message.className = 'diagram-notice';
      message.textContent = 'Diagram renderer could not load. Read the source and explanation below; an internet connection is needed for the renderer.';
      block.parentElement.before(message);
    }
    console.error('Mermaid failed to load', error);
    return;
  }
  for (const [index, block] of blocks.entries()) {
    const source = block.textContent;
    const pre = block.parentElement;
    const figure = document.createElement('figure');
    figure.className = 'course-diagram';
    pre.replaceWith(figure);
    const details = document.createElement('details');
    const summary = document.createElement('summary');
    summary.textContent = 'View Mermaid source';
    details.append(summary, pre);
    try {
      const { svg } = await mermaid.render(`course-diagram-${index}`, source);
      const canvas = document.createElement('div');
      canvas.className = 'diagram-canvas';
      canvas.innerHTML = svg;
      figure.append(canvas, details);
      figure.dataset.state = 'rendered';
    } catch (error) {
      const notice = document.createElement('p');
      notice.textContent = 'Diagram could not render. Its source is shown below.';
      notice.className = 'diagram-notice';
      details.open = true;
      figure.append(notice, details);
      figure.dataset.state = 'error';
      console.error('Mermaid diagram failed', error);
    }
  }
})();
