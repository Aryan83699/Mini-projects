import React from 'react'
import Note from './Note'

const Right = (props) => {

 const notes = props.note;
 console.log(notes);

  return (
    <div className=' h-full w-6/10 overflow-y-auto p-4 flex shrink-0 flex-wrap gap-5'>
      
    {notes.map((note, idx) => (
        <Note
            key={idx}
            id={note.id}
            title={note.title}
            description={note.description}
        />
    ))}


    </div>
  )
}

export default Right