import React, { useState } from 'react'

const Left = (props) => {

    const [title , settitle]=useState("");
    const [desc , setdesc]=useState("");

    function changeTitle(e){
        // console.log(e.target.value);
        settitle(e.target.value);

    }

    function changeDesc(e){
        // console.log(e.target.value);
        setdesc(e.target.value);
    }

   function postData(e) {
        e.preventDefault();
        props.addnote(prev => [
            ...prev,
            {
                id: `${JSON.stringify(new Date().getDate())}/${JSON.stringify(new Date().getMonth())}/${JSON.stringify(new Date().getFullYear())}`,
                title: title,
                description: desc
            }
        ]);
        settitle("");
        setdesc("");
    }


  return (
    <div className=' p-5 w-2/5 flex flex-col bg-amber-50 gap-5'>
        <h1 className="font-medium text-black text-xl">Note Taking.....</h1>
        <input value={title} onChange={changeTitle} type="text" placeholder='title of note...'  className='border hover:border-amber-600  border-gray-600 rounded-md p-3' autoFocus />
        <textarea value={desc}  onChange={changeDesc} placeholder='content of note...'  className='border hover:border-amber-600 border-gray-600 rounded-md  py-5 px-5 flex flex-col justify-start align-top' rows="10" />
        <button onClick={postData} className='border cursor-pointer border-amber-300 bg-red-400 py-3 px-4 text-center font-semibold text-white text-md rounded-md active:scale-95'>Submit</button>
    </div>
  )
}

export default Left