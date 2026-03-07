"use client"

import { useState } from "react"

export default function MediaLibrary({ editor }){

const [image,setImage] = useState(null)

const generateAIImage = ()=>{

fetch("http://127.0.0.1:8000/generate-image",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
prompt:"restaurant hero banner"
})

})
.then(res=>res.json())
.then(data=>{

const url = "http://127.0.0.1:8000"+data.url

const selected = editor.getSelected()

if(selected){

selected.addAttributes({
src:url
})

}

})

.catch(err=>{

console.log("Image API error",err)

})

}
const upload = async ()=>{

if(!image) return

const form = new FormData()

form.append("file",image)

const res = await fetch("http://127.0.0.1:8000/upload-image",{

method:"POST",
body:form

})

const data = await res.json()

if(editor){

const selected = editor.getSelected()

if(selected){

selected.addAttributes({

src:data.url

})

}

}

}

return(

<div style={{
width:"250px",
borderLeft:"1px solid #ddd",
padding:"10px"
}}>

<h3>Media Library</h3>

<input
type="file"
onChange={(e)=>setImage(e.target.files[0])}
/>

<button
onClick={upload}
style={{
marginTop:"10px",
padding:"6px 12px"
}}
>

Upload Image

</button>
<button
onClick={generateAIImage}
style={{
marginTop:"10px",
padding:"6px 12px",
background:"purple",
color:"white"
}}
>

AI Generate Image

</button>
</div>

)

}