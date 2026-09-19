import React from 'react';

const Card = (props) => {
  return (
    <div className="sm:h-[60vh] sm:w-[50vw]  md:h-[40vh] md:w-[15vw]  bg-white rounded-lg shadow-md shadow-black relative flex flex-wrap shrink-0 overflow-x-hidden ">
        <div className="top h-[9.75vh] w-full  rounded-t-lg p-1">
            {/* <h2 className='text-white font-medium text-xs '>{props.company}</h2> */}
            <img src={props.companyURL} alt="" className="object-top" />
        </div>
        <div className="bottom h-[30vh] w-full bg-gray-50 flex flex-col gap-2 justify-between items-center rounded-b-lg p-1.5">
            <div className="mt-12.5 details flex flex-col items-center">
                            <p className="name text-black font-bold text-sm p-1" >
                                {props.name}
                            </p>
                            <p className="description text-xs font-light text-center ">
                                {props.description}
                            </p>
            </div>

            <div className="extras flex gap-5 shrink-0">
                <button className='font-extrabold text-[0.5rem] font-mono border text-green-600 border-green-400 rounded-md px-1 py-0.5'>{props.available}</button>
                <button className='font-extrabold text-[0.5rem] font-mono px-1 py-0.5'><i className="fa-solid fa-location-dot"></i> {props.location}</button>
                <button className='font-extrabold text-[0.5rem] bg-amber-200 font-mono border text-red-600 border-orange-400 rounded-full px-1 py-0.5'>#{props.rank}</button>
            </div>


            

        </div>

        
            <img src={props.pfp} alt=""  className="absolute top-10 left-1/2 h-20 w-20 -translate-x-1/2 rounded-full border-2 border-gray-600"  />
        


    </div>
  )
}

export default Card