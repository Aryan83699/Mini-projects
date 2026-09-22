import React, { useEffect } from 'react'
import Note from './Note'

const Right = (props) => {

 const notes = props.note;
 

let message="";

 useEffect(()=>{
  <h1 className='text-2xl'>No Data</h1>
 },[])

  return (
    <div className=' h-full w-6/10 overflow-y-auto p-4 flex shrink-0 flex-wrap gap-5'>
      
      {notes.length === 0 ? (
        <h1 className="text-5xl font-extrabold text-white m-auto">No Data</h1>
      ) : (
        notes.map((note, idx) => (
          <Note
            key={idx}
            id={note.id}
            title={note.title}
            description={note.description}
            delnote={props.addnote}
            notess={props.note}
            idx={idx}
          />
        ))
      )}

    </div>
  )
}

export default Right