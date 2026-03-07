"use client"

import { useEffect, useState } from "react"
import { API_URL } from "../../services/api"

export default function SectionLibrary({ editor }) {

const [sections,setSections] = useState([])

useEffect(()=>{

fetch(API_URL + "/sections")
.then(res=>res.json())
.then(data=>setSections(data))

},[])

const addSection = (html)=>{

if(!editor) return

editor.addComponents(html)

}

return(

<div style={{
width:"300px",
overflow:"auto",
borderRight:"1px solid #ddd"
}}>

<h3 style={{padding:"10px"}}>Section Library</h3>

{sections.map((sec)=>(
<div
key={sec.id}
style={{
padding:"10px",
cursor:"pointer",
borderBottom:"1px solid #eee"
}}
onClick={()=>addSection(sec.html_code)}
>
{sec.name}
</div>
))}

</div>

)

}