import express from "express";
import { spawn } from "child_process";
const app = express(); 

app.get("/", (req,res)=>{
    res.send("hello world");
})

app.get("/live", (req, res) => {
    const python = spawn('python', ['/home/harshini/Desktop/WEBCAM/object_detection_phone.py']);
  
    let dataToSend = "";
    python.stdout.on("data", (data) => {
      dataToSend += data.toString();
    });
  
    python.on("close", (code) => {
      console.log(`Python exited with code ${code}`);
      res.send(`<pre>${dataToSend}</pre>`); 
    });
    python.stderr.on("data", (data) => {
      console.error(`Error: ${data}`);
    });
  });
  
app.listen(5000, console.log("Server is listening at PORT 5000"));