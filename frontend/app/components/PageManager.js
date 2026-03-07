"use client"

export default function PageManager({ pages, loadPage }) {

if(!pages) return null

return (

<div style={{
width:"200px",
borderRight:"1px solid #ddd",
padding:"10px"
}}>

<h3>Pages</h3>

{Object.keys(pages).map((page)=>(
<div
key={page}
style={{
padding:"6px",
cursor:"pointer",
borderBottom:"1px solid #eee"
}}
onClick={()=>loadPage(page)}
>

{page}

</div>
))}

</div>

)

}