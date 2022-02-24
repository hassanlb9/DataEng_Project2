import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useState } from 'react';


function App() {
  const [text,setText]=useState("");
  async function post_text(e){

try{

  await axios.post("http://localhost:4000/post_text",
  {text}
  
  )
} catch(error){
  console.log(error)
}
  }


  return (
<body>
<div class="container">
    <div class="container-lg">
        <h1 class="title"> Sentiment Analysis </h1>
        <form method="POST" onSubmit={post_text}>
          <textarea type="text" value={text} name="inp" placeholder="Enter your feelings ! " id="inp"></textarea>
            <input type="submit" name="submit" id="btn" class="btn btn-primary"></input>

        </form>
     
       

    </div>
</div>
</body>
  );
}

export default App;
