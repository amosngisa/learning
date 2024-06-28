import Book from './Book.jsx'
import MasteringReact from './mastering react.svg'
import LearningHtml from './practical react.svg'
import JavaScriptEs6 from './react in action.svg'

const App = () =>{
  return(
    <main>
      <h1>Favorite Books</h1>
      <br />
      <Book title="Mastering React" author="Amos Ngisa" cover={MasteringReact}/>
      <Book title="Learning HTML & CSS" author="Mozila Firefox" cover={LearningHtml}/>
      <Book title="JavaScript ES6" author="Zindual School" cover={JavaScriptEs6}/>
    </main>
  )
}

export default App