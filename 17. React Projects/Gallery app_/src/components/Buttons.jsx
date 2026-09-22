import React from 'react'

const Buttons = (props) => {

  

  function increment(){
    props.changePage(props.pageNum+1);
  }
  
  function decrement(){
    props.changePage(props.pageNum-1);
  }
  


  return (
    <div className='flex justify-center gap-5  items-center mx-auto w-full'>
        {props.pageNum==1?<button disabled onClick={decrement} className="bg-blue-600 text-white text-lg font-bold font-mono py-2 px-4.5 rounded-lg opacity-35">Prev</button>:<button onClick={decrement} className="bg-blue-600 text-white text-lg cursor-pointer font-bold font-mono py-2 px-4.5 rounded-lg">Prev</button>}
        <p className="text-white font-bold text-lg">Page:- {props.pageNum}</p>
        <button onClick={increment} className="bg-blue-600 text-white text-lg font-bold cursor-pointer font-mono py-2 px-4.5 rounded-lg">Next</button>
    </div>
  )
}

export default Buttons