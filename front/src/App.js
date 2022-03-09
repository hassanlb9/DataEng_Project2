import logo from './logo.svg';
import './App.css';
import Nav from "./component/Form.js"

import { useState } from 'react';

function POST(path, data) {
  return fetch(`${path}`,
  {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }
  )
}

function App(props) {
  const [text, setText] = useState('');
  const [name, setName] = useState('');
    const onChange = e => {
      setText(e.target.value)
    }
    const onClick = e => {
      e.preventDefault();
      POST('/post_text', {name: text}).then(
        async (resp) => {
          const json= await resp.json()
          console.log(json.name)
          setName(json.name)
        }
      )
    }


  

  return (

<div class="container">
    <div class="container-lg">
        <h1 class="title"> Sentiment Analysis </h1>
        <form>
          <textarea type="text" value={text}   onChange={onChange} name="inp" id="inp" placeholder="Enter your feelings ! "/>
            <input type="submit" value="Submit" onClick={onClick} name="submit" id="btn" class="btn btn-primary"/>

        </form>
       
     
        

    </div>
    <Nav/>
</div>


  );
}

export default App;
