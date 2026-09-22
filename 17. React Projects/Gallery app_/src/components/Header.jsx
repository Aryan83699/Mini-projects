import React from 'react'

const Header = () => {
  return (
      <div className="w-full rounded-lg relative">
        <img src="https://images.pexels.com/photos/14757356/pexels-photo-14757356.jpeg" alt="bg" className='w-full h-[50vh] object-cover align-middle rounded-xl' />
        <p className='absolute top-1/3 left-1/4 translate-x-5 text-center font-bold text-white text-5xl font-sans '>Image Gallery with ReactJs</p>
      </div>
  )
}

export default Header