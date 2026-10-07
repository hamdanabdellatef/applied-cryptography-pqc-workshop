import fs from 'node:fs/promises';
import path from 'node:path';
import puppeteer from 'puppeteer';
import {renderMermaid} from '@mermaid-js/mermaid-cli';
const [manifest, output, executablePath] = process.argv.slice(2);
const diagrams = JSON.parse(await fs.readFile(manifest, 'utf8'));
const browser = await puppeteer.launch(executablePath ? {executablePath} : {});
try {
  for (const [id, definition] of Object.entries(diagrams)) {
    const {data} = await renderMermaid(browser, definition, 'png', {
      viewport:{width:1400,height:900,deviceScaleFactor:1.5}, backgroundColor:'white',
      mermaidConfig:{theme:'neutral',securityLevel:'strict',flowchart:{htmlLabels:false},fontFamily:'Arial'}
    });
    await fs.writeFile(path.join(output,id+'.png'),data);
    console.log('Rendered',id);
  }
} finally {await browser.close();}
