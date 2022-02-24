import logo from './logo.svg';
import './App.css';

function App() {
  return (
<body>
<div class="container">
    <div class="container-lg">
        <h1 class="title"> Sentiment Analysis </h1>
        <form method="POST" class="form">
          <textarea type="text" name="inp" placeholder="Enter your feelings ! " id="inp"></textarea>
            <input type="submit" name="submit" id="btn" class="btn btn-primary"></input>

        </form>
     
       

    </div>
</div>
</body>
  );
}

export default App;
