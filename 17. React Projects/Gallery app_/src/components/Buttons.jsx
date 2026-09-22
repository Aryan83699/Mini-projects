import React from 'react'

const Buttons = () => {
  return (
    <div className='flex justify-center gap-5  items-center mx-auto w-full'>
        <button className="bg-blue-600 text-white text-lg font-bold font-mono py-2 px-4.5 rounded-lg">Prev</button>
        <button className="bg-blue-600 text-white text-lg font-bold font-mono py-2 px-4.5 rounded-lg">Next</button>
    </div>
  )
}

export default Buttons