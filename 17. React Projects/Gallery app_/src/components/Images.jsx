
import React, { useEffect, useRef, useState } from 'react'
import Card from './Card';

const Images = (props) => {

 let imagesData=props.data;

  return (
    <div className=" py-10 flex gap-3 flex-wrap shrink-0">
        {/* <button className='cursor-pointer rounded-lg bg-amber-100 text-xl font-bold p-5 ' onClick={getData}>Click Me </button> */}
        {imagesData.map(
            (elem) =>{
                return (
                    <Card key={elem.id} author={elem.author} link={elem.download_url} url={elem.url}></Card>
                )
            }
        )}

        
    </div>
  )
}

export default Images