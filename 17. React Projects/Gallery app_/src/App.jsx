import React, { useEffect, useState } from 'react';
import Header from './components/Header';
import Images from './components/Images';
import axios from 'axios';
import Buttons from './components/Buttons';

const App = () => {

    const [useData , setuserData]=useState([]);

    async function getData(){
      let response = await axios.get("https://picsum.photos/v2/list?page=32&limit=15");
      setuserData(response.data);
    }

   useEffect(()=>{
    getData();
   },[])



  return (
    <div className='min-h-screen w-full bg-black p-5'>
      <Header />
      <Images data={useData}></Images>
      <Buttons></Buttons>
      
    </div>
  )
}

export default App