from pathlib import Path
import xml.etree.ElementTree as ET
p=Path(__file__).parent
images=['https://cdn.prod.website-files.com/64dfd6f3c8bff842f83e0e0e/6aad6c185e44c39a92c8e582_forgif-ezgif.com-video-to-gif-converter.gif', 'https://cdn.prod.website-files.com/64dfd6f3c8bff842f83e0e0e/6a28afbc5b93f9f574f078fc_img.png', 'https://cdn.prod.website-files.com/64dfd6f3c8bff842f83e0e0e/697a93ac799598973f982768_forgif-ezgif.com-optimize.gif', 'https://cdn.prod.website-files.com/64dfd6f3c8bff842f83e0e0e/67ebe520d5174e0cbf16829f_Frame%203123.jpg', 'https://cdn.prod.website-files.com/64dfd6f3c8bff842f83e0e0e/67e967495a56e134f60784d7_OpenBox_Honeycomb%202.jpg']
images=images[:3]
ET.register_namespace('', 'http://www.w3.org/2000/svg')
source=ET.parse(p/'assets/logo.svg').getroot()
paths=list(source)
def word(start,end,viewbox):
    node=ET.Element('{http://www.w3.org/2000/svg}svg', {'viewBox':viewbox,'aria-hidden':'true','class':'av-word'})
    for path in paths[start:end]: node.append(path)
    return ET.tostring(node,encoding='unicode')
left=word(0,7,'0 0 195.3 48')
right=word(7,11,'209.5 0 160.5 48')
css='''<style>
.av-work,.av-work *{box-sizing:border-box}
.av-work{--av-logo-width:clamp(240px,42vw,400px);--av-gallery-width:clamp(220px,34vw,340px);width:100%;height:var(--av-height,90svh);min-height:420px;display:grid;place-items:center;overflow:hidden;background:transparent;padding:0 clamp(24px,6vw,96px)}
.av-stage{display:flex;align-items:center;justify-content:center;text-decoration:none;color:#000;padding:110px 16px;outline-offset:12px;cursor:pointer;-webkit-tap-highlight-color:transparent}
.av-left{width:calc(var(--av-logo-width)*.528);flex:none}
.av-right{width:calc(var(--av-logo-width)*.434);flex:none}
.av-word{display:block;width:100%;height:auto}
.av-gallery{display:flex;align-items:center;justify-content:center;width:calc(var(--av-logo-width)*.038);height:250px;flex:none;overflow:hidden;transition:width 850ms cubic-bezier(.22,1,.36,1);position:relative}
.av-strip{width:var(--av-gallery-width);display:flex;align-items:center;justify-content:center;gap:7px;flex:none;padding:0 12px;opacity:0;transform:scale(.75);transition:opacity 350ms ease,transform 850ms cubic-bezier(.22,1,.36,1)}
.av-stage[data-open] .av-gallery{width:var(--av-gallery-width)}
.av-stage[data-revealed] .av-gallery{overflow:visible;z-index:3}
.av-stage:not([data-open]) .av-strip{pointer-events:none}
.av-stage[data-open] .av-strip{opacity:1;transform:scale(1);transition-delay:120ms}
.av-project{display:block;width:9%;height:66px;object-fit:cover;flex:1;min-width:0;position:relative;filter:grayscale(1);transform:scale(1);transition:filter 400ms ease,transform 650ms cubic-bezier(.22,1,.36,1),height 650ms cubic-bezier(.22,1,.36,1),flex 650ms cubic-bezier(.22,1,.36,1),width 650ms cubic-bezier(.22,1,.36,1),flex-basis 650ms cubic-bezier(.22,1,.36,1);user-select:none}
.av-project[data-active]{flex:5;height:220px;object-fit:contain}
.av-project[data-enlarged]{filter:grayscale(0);width:100px;flex:0 0 100px;height:100px;object-fit:contain;transform:scale(3);z-index:5}
@media(max-width:600px){.av-work{--av-logo-width:48vw;--av-gallery-width:36vw;padding-inline:12px}.av-stage{padding:90px 4px}.av-gallery{height:210px}.av-strip{gap:3px;padding-inline:7px}.av-project{height:38px}.av-project[data-active]{height:165px;flex:8}.av-project[data-enlarged]{width:60px;flex:0 0 60px;height:60px}}
@media(prefers-reduced-motion:reduce){.av-work *{transition:none!important}}
</style>'''
markup='<section class="av-work" aria-label="Explore Aashita Verma’s work"><a class="av-stage" href="https://www.aashitaverma.com/work" target="_top" aria-label="View Aashita Verma’s work"><span class="av-left">'+left+'</span><span class="av-gallery"><span class="av-strip">'+''.join(f'<img class="av-project" src="{url}" alt="Project preview {i+1}" draggable="false"'+'>' for i,url in enumerate(images))+'</span></span><span class="av-right">'+right+'</span></a></section>'
js='''<script>
(()=>{if(window.parent!==window){const allowedParents=['https://www.aashitaverma.com','https://aashitaverma.com','https://aashitaverma.webflow.io'];let parentOrigin;try{const origin=new URL(document.referrer).origin;if(allowedParents.includes(origin))parentOrigin=origin}catch{}document.addEventListener('pointermove',e=>{const message={type:'aashita-logo:pointermove',x:e.clientX,y:e.clientY};if(parentOrigin){window.parent.postMessage(message,parentOrigin)}else{allowedParents.forEach(origin=>window.parent.postMessage(message,origin))}},{passive:true})}const root=document.currentScript.previousElementSibling;const stage=root.querySelector('.av-stage');const projects=[...root.querySelectorAll('.av-project')];const reduced=matchMedia('(prefers-reduced-motion: reduce)');let timer;let revealTimer;let hovering=false;let focused=false;let nextFeatured=0;function featureNext(){projects.forEach((p,i)=>p.toggleAttribute('data-active',i===nextFeatured));nextFeatured=(nextFeatured+1)%projects.length}function schedule(fn,delay){clearTimeout(timer);if(!reduced.matches)timer=setTimeout(fn,delay)}function open(){if(!stage.hasAttribute('data-open'))featureNext();stage.setAttribute('data-open','');clearTimeout(revealTimer);revealTimer=setTimeout(()=>stage.setAttribute('data-revealed',''),850);schedule(close,6000)}function close(){if(hovering||focused)return;stage.removeAttribute('data-revealed');stage.removeAttribute('data-open');projects.forEach(p=>p.removeAttribute('data-enlarged'));schedule(open,5000)}projects.forEach(p=>{p.addEventListener('pointerenter',e=>{if(e.pointerType==='touch'||!stage.hasAttribute('data-open'))return;hovering=true;clearTimeout(timer);projects.forEach(other=>other.toggleAttribute('data-enlarged',other===p))});p.addEventListener('pointerleave',()=>{hovering=false;p.removeAttribute('data-enlarged');schedule(close,3000)})});stage.addEventListener('focus',()=>{focused=true;open();clearTimeout(timer)});stage.addEventListener('blur',()=>{focused=false;schedule(close,3000)});stage.addEventListener('keydown',e=>{if(e.key==='Escape'){hovering=false;focused=false;clearTimeout(timer);clearTimeout(revealTimer);stage.removeAttribute('data-revealed');stage.removeAttribute('data-open');projects.forEach(p=>p.removeAttribute('data-enlarged'));schedule(open,5000)}});function start(){clearTimeout(timer);clearTimeout(revealTimer);if(reduced.matches){featureNext();stage.setAttribute('data-open','');stage.setAttribute('data-revealed','')}else schedule(open,1800)}reduced.addEventListener('change',start);start();})();
</script>'''
embed=css+markup+js
(p/'section-source.html').write_text(embed)
(p/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aashita Verma — Work Preview</title><style>body{margin:0;background:transparent}.av-work{--av-height:100svh}</style>'+embed+'</html>')
