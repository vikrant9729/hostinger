"use client"

export default function StyleEditor({ editor }){

const changeColor = (color)=>{

if(!editor) return

const selected = editor.getSelected()

if(selected){

selected.addStyle({

"color":color

})

}

}

const changeBackground = (color)=>{

if(!editor) return

const selected = editor.getSelected()

if(selected){

selected.addStyle({

"background-color":color

})

}

}

return(

<div style={{
width:"250px",
borderLeft:"1px solid #ddd",
padding:"10px"
}}>

<h3>Style Editor</h3>

<p>Text Color</p>

<input
type="color"
onChange={(e)=>changeColor(e.target.value)}
/>

<p>Background</p>

<input
type="color"
onChange={(e)=>changeBackground(e.target.value)}
/>

</div>

)

}