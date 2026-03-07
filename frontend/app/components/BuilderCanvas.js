"use client"

import { useEffect } from "react"
import grapesjs from "grapesjs"
import "grapesjs/dist/css/grapes.min.css"

export default function BuilderCanvas({ setEditor }) {

useEffect(() => {

const editorInstance = grapesjs.init({

container: "#editor",

height: "100vh",

storageManager: false,

undoManager: true

})

// Mobile + Tablet preview
editorInstance.DeviceManager.add("Mobile", "320px")
editorInstance.DeviceManager.add("Tablet", "768px")

// Parent component को editor भेजना
setEditor(editorInstance)

}, [])

return (

<div id="editor"></div>

)

}