"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"

export default function Login(){

const router = useRouter()

const [email,setEmail] = useState("")
const [password,setPassword] = useState("")

const login = ()=>{

fetch("http://127.0.0.1:8000/login",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

email:email,
password:password

})

})
.then(res=>res.json())
.then(data=>{

if(data.user){

localStorage.setItem("user",JSON.stringify(data.user))

router.push("/dashboard")

}

})

}

return(

<div style={{padding:"100px"}}>

<h2>Login</h2>

<input
placeholder="Email"
onChange={(e)=>setEmail(e.target.value)}
/>

<br/>

<input
placeholder="Password"
type="password"
onChange={(e)=>setPassword(e.target.value)}
/>

<br/>

<button onClick={login}>Login</button>

</div>

)

}