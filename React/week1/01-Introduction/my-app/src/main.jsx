import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

// //import RickyAndMorty from './Hook'
// import {BrowserRouter} from 'react-router-dom'//react-router-dom import
// import './App.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <BrowserRouter> */}
      <App />
    {/* </BrowserRouter> */}
    
  </React.StrictMode>,
)

//BrowserRouter - web applications
//HashRouter - static sites

//Key concepts
// 1. Route - mapping btn url and component
// 2. Router - top-level infra thatprovides routing (BrowserRoiuter)
// 3. Nested Routes - hierachy of compnents
// 4. Link - enables navigation