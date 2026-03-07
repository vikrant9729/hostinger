"use client"

import { useState, useEffect } from "react"

import SectionLibrary from "../components/SectionLibrary"
import BuilderCanvas from "../components/BuilderCanvas"
import StyleEditor from "../components/StyleEditor"
import MediaLibrary from "../components/MediaLibrary"
import PageManager from "../components/PageManager"
import { useSearchParams } from "next/navigation"

export default function Editor(){

const [editor,setEditor] = useState(null)
const [prompt,setPrompt] = useState("")
const [aiInstruction, setAiInstruction] = useState("")
const [pages,setPages] = useState({})
const searchParams = useSearchParams()
const siteId = searchParams.get("id")

const generateSite = ()=>{
    fetch("http://127.0.0.1:8000/generate-site",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({prompt:prompt})
    })
    .then(res=>res.json())
    .then(data=>{
        editor.setComponents(data.html);
        if (data.pages) {
            setPages(data.pages);
        }
    })
}

const editWithAi = () => {
    if (!editor || !aiInstruction) return
    const selected = editor.getSelected()
    if (!selected) {
        alert("Please select an element to edit with AI")
        return
    }
    
    const html = selected.toHTML()
    fetch("http://127.0.0.1:8000/edit-with-ai", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            prompt: aiInstruction,
            html: html
        })
    })
    .then(res => res.json())
    .then(data => {
        selected.replaceWith(data.html)
        setAiInstruction("")
    })
}

useEffect(()=>{

if(!siteId) return

fetch("http://127.0.0.1:8000/site/"+siteId)
.then(res=>res.json())
.then(data=>{

if(editor){

editor.setComponents(data.html)

}

})

},[editor])

const generateSections = ()=>{

fetch("http://127.0.0.1:8000/generate-sections",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

prompt:prompt

})

})
.then(res=>res.json())
.then(()=>{

alert("AI Sections Created")

})

}

// save website
const saveSite = ()=>{

if(!editor) return

const html = editor.getHtml()
const css = editor.getCss()

fetch("http://127.0.0.1:8000/save-site",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

name:"my-site",
html:html,
css:css

})

})
.then(res=>res.json())
.then(()=>{

alert("Website Saved")

})

}

const loadPage = (page)=>{

if(editor){

editor.setComponents(pages[page])

}

}

// publish website
const publishSite = ()=>{

if(!editor) return

const html = editor.getHtml()
const css = editor.getCss()

fetch("http://127.0.0.1:8000/publish",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

name:"my-site",
html:html,
css:css

})

})
.then(res=>res.json())
.then(data=>{

alert("Website Published: "+data.url)

})

}

return(

<div style={{display:"flex",height:"100vh",flexDirection:"column"}}>

{/* NAVBAR */}

<div style={{
height:"60px",
background:"#1e1e1e",
color:"white",
display:"flex",
alignItems:"center",
padding:"0 20px",
justifyContent:"space-between"
}}>

<div style={{fontWeight:"bold",fontSize:"20px"}}>
AI Builder Pro
</div>

<div style={{display:"flex",alignItems:"center",gap:"10px"}}>
    <input 
        type="text" 
        placeholder="Build whole site with one prompt..." 
        value={prompt}
        onChange={(e)=>setPrompt(e.target.value)}
        style={{padding:"8px", borderRadius:"4px", border:"none", width:"300px", color:"black"}}
    />
    <button onClick={generateSite} style={{padding:"8px 15px", background:"#007bff", color:"white", border:"none", borderRadius:"4px", cursor:"pointer"}}>
        Build Site
    </button>
</div>

<div style={{display:"flex",alignItems:"center",gap:"10px"}}>
    <input 
        type="text" 
        placeholder="Edit selected with AI..." 
        value={aiInstruction}
        onChange={(e)=>setAiInstruction(e.target.value)}
        style={{padding:"8px", borderRadius:"4px", border:"none", width:"200px", color:"black"}}
    />
    <button onClick={editWithAi} style={{padding:"8px 15px", background:"#28a745", color:"white", border:"none", borderRadius:"4px", cursor:"pointer"}}>
        AI Edit
    </button>
</div>

<div>

<button
onClick={saveSite}
style={{marginRight:"10px"}}
>
Save
</button>

<button
onClick={()=>editor?.setDevice("Desktop")}
style={{marginRight:"10px"}}
>
Desktop
</button>

<button
onClick={()=>editor?.setDevice("Mobile")}
style={{marginRight:"10px"}}
>
Mobile
</button>

<button onClick={publishSite}>
Publish
</button>

</div>

</div>

{/* MAIN AREA */}

<div style={{display:"flex",flex:1,overflow:"hidden"}}>

{/* LEFT PANEL */}

<div style={{width:"280px",background:"#f8f9fa",borderRight:"1px solid #ddd",display:"flex",flexDirection:"column", overflowY:"auto"}}>
<PageManager pages={pages} onSelectPage={loadPage}/>
<SectionLibrary editor={editor}/>
</div>

{/* BUILDER */}

<div style={{flex:1, position:"relative"}}>
<BuilderCanvas setEditor={setEditor}/>
</div>

{/* RIGHT PANEL */}

<div style={{width:"280px",background:"#f8f9fa",borderLeft:"1px solid #ddd",overflowY:"auto"}}>
<StyleEditor editor={editor}/>
<MediaLibrary editor={editor}/>
</div>

</div>

</div>

)

}
