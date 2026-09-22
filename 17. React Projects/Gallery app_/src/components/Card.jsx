import React from 'react'

const Card = (props) => {
  return (
    <div className='card p-2'>
        <a href={props.url} className='relative'>
            <img src={props.link} alt="" className='object-cover h-60 w-60 rounded-lg opacity-75' />
            <p className='absolute text-white font-bold text-md font-sans bottom-5 left-5 text-shadow-black'>{props.author}</p>
        </a>
        
    </div>
  )
}

export default Card