
import React,{useEffect,useState} from 'react';
import {Link} from 'react-router-dom';
function Connect() {
    useEffect( () => {
        fetchItems();
    }, []);
    const [items, setItems]= useState([]);
    const fetchItems= async () => {
       const data= await fetch('/post_text');//retrieve data on the back end side
       const items= await data.json();//recgnize those data which are in the json format
       setItems(items);
    };

  return ( 
    <section>
      {
         items.map(e => (
        <div>
        <p>toxicity:{e.toxicity}</p>
        <p>severe_toxicity:{e.severe_toxicity}</p>
        <p>identity_attack:{e.identity_attack}</p>
        <p>obscene:{e.obscene}</p>
        <p>threat:{e.threat}</p>
        <p>insult:{e.insult}</p>
        <p>identity_attack:{e.identity_attack}</p>

        
        

        </div>
        
 ))
    
    }
    </section>);
}

export default  Connect;
