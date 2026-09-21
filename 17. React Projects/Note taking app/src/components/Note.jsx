import React from 'react'

const Note = (props) => {

    const colors=['bg-yellow-200','bg-gray-300']

  return (
    <div className="bg-yellow-300 rounded-lg h-80 w-62.5 px-2 py-2.5  flex flex-col gap-3.5">
        <p className='text-black font-bold font-mono leading-4.5'>Title :- <br></br>{props.title}</p>
        <p className='text-black text-sm font-mono leading-4.5'><b>Description :-</b> <br></br>{props.description}</p>
    </div>
  )
}

export default Note