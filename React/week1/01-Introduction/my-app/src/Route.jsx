import {Route, Routes} from 'react-router-dom'
import Home from './Home'
import About from './About'
import Contact from './Contact'
import ErrorPage from './error-page'
import './index.css'

const App = () =>{

    return(
        <div className='App'>
            <Routes>
                <Route path='/' element={<Home/>} errorElement={<ErrorPage />} />
                <Route path='/about' element={<About/>} />
                <Route path='/contact/:id' element={<Contact/>} errorElement={<ErrorPage />} />
            </Routes>

        </div>
    )
}

export default App