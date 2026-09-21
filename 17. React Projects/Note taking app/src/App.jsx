import React, { useState } from 'react'
import Left from './components/Left'
import Right from './components/Right'
import './index.css'

const App = () => {

  const [notes , setnote] = useState([]);

  return (
    <div className="h-screen w-full flex gap-1 bg-gray-600">
      <Left addnote={setnote}/>
      <Right note={notes}/>
    </div>
  )
}

export default App
