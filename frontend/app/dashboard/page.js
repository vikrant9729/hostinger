"use client"

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"

export default function Dashboard(){

const router = useRouter()

const [sites,setSites] = useState([])
const [user,setUser] = useState(null)

useEffect(()=>{

const storedUser = localStorage.getItem("user")

if(storedUser){

const parsedUser = JSON.parse(storedUser)

setUser(parsedUser)

fetch("http://127.0.0.1:8000/websites/"+parsedUser.id)
.then(res=>res.json())
.then(data=>{

setSites(data)

})

}

},[])

const deleteSite = (id)=>{

fetch("http://127.0.0.1:8000/delete-website/"+id,{

method:"DELETE"

})
.then(()=>{

setSites(sites.filter(s=>s.id!==id))

})

}

return(

<div style={{padding:"40px"}}>

<h2>My Websites</h2>

<button
onClick={()=>router.push("/editor")}
style={{
marginBottom:"20px",
padding:"8px 15px"
}}
>

Create Website

</button>

{sites.map((site)=>(

<div key={site.id}
style={{
border:"1px solid #ddd",
padding:"10px",
marginBottom:"10px"
}}
>

<h3>{site.name}</h3>

<button
onClick={()=>router.push("/editor?id="+site.id)}
style={{marginRight:"10px"}}
>

Edit

</button>

<button
onClick={()=>deleteSite(site.id)}
>

Delete

</button>

</div>

))}

</div>

)

}