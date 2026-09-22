import React from 'react'

const Card = (props) => {
  return (
    <div className='card p-2 shadow-sm shadow-gray-500 rounded-lg'>
        <a href={props.url} className='relative'>
            <img src={props.link} alt="" className='object-cover h-60 w-60 rounded-lg opacity-75' />
            <div className='absolute rounded-b-lg text-white font-bold text-sm font-sans bottom-0 left-0 py-1 pl-2 text-shadow-black bg-gray-700 opacity-80 w-full'>
              <p >{props.author}</p>
            </div>
        </a>
        
    </div>
  )
}

export default Card