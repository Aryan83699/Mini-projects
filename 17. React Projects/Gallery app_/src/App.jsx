import React, { useEffect, useState } from 'react';
import Header from './components/Header';
import Images from './components/Images';
import axios from 'axios';
import Buttons from './components/Buttons';

const App = () => {

    const [useData , setuserData]=useState([]);
    const [page , setPage]=useState(1);

    async function getData(page){
      let response = await axios.get(`https://picsum.photos/v2/list?page=${page}&limit=15`);
      setuserData(response.data);
    }

   useEffect(()=>{
    getData(page);
   },[page])

  
  
   

  return (
    <div className='min-h-screen w-full bg-[#16213E] p-5'>
      <Header />
      <Images data={useData}></Images>
      <Buttons pageNum={page} changePage={setPage}></Buttons>
      
    </div>
  )
}

export default App