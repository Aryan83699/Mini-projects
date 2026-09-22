import React from 'react'

const Note = (props) => {

    const colors=["#7FFFD4","#FFF8DC","#8FBC8F","#FFFAF0","#F0E68C"]

    function randColor(){
      const color=colors[Math.floor(Math.random()*colors.length)];
      return color;
    }

    function deleteNote(idx){
      let totalnotes=props.notess;
      const copynotes=[...totalnotes];
      copynotes.splice(idx,1)

      props.delnote(
        copynotes
      )

    }

  return (
    <div className=" rounded-lg h-80 w-62.5 px-2 py-2.5  flex flex-col gap-3.5 justify-between" style={{backgroundColor:randColor()}}>
      <div className="top flex flex-col gap-1">
        <p className='text-black font-bold font-mono leading-5.5'>Title :- <br></br>{props.title}</p>
        <p className='text-black text-sm font-mono leading-5.5'><b>Description :-</b> <br></br>{props.description}</p>
      </div>
      <div className="bottom flex flex-col gap-3.5">
        <p className='text-black text-sm font-mono leading-4.5'><b>Date :-</b>{props.id}</p>
        <button onClick={() => { deleteNote(props.idx) }}className='rounded-lg cursor-pointer bg-red-400 text-white font-extrabold text-md py-1 w-1/2 m-auto border-1 border-white px-4.5'>Cancel</button>
      </div>
    </div>
  )
}

export default Note