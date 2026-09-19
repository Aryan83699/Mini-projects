import React from 'react';
import Card from './components/Card';


function App() {



  const heroes = [
  {
    name: "Superman",
    description:
      "A Kryptonian hero with incredible strength, speed, flight, heat vision, and near-invulnerability.",
    available: "Available",
    location: "Metropolis",
    rank: 10,
    company: "DC",
    companyImageUrl:
      "https://tse2.mm.bing.net/th/id/OIP.rJkRHRfdcZDy1BGH5D0Y8AHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl:
      "https://upload.wikimedia.org/wikipedia/en/3/35/Supermanflying.png",
  },

  {
    name: "Thor",
    description:
      "The Asgardian God of Thunder who wields Mjolnir and commands powerful lightning.",
    available: "Available",
    location: "Asgard",
    rank: 10,
    company: "Marvel",
    companyImageUrl:
      "https://upload.wikimedia.org/wikipedia/commons/b/b9/Marvel_Logo.svg",
    imageUrl:
      "https://tse3.mm.bing.net/th/id/OIP.f3ZAK1UG11Rt6y5SASw0MQAAAA?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Batman",
    description:
      "A highly trained detective and martial artist who uses intelligence, strategy, and advanced technology.",
    available: "Available",
    location: "Gotham City",
    rank: 7,
    company: "DC",
    companyImageUrl:
      "https://tse2.mm.bing.net/th/id/OIP.rJkRHRfdcZDy1BGH5D0Y8AHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl:
      "https://tse2.mm.bing.net/th/id/OIP.0bFNN9B1QSbKFQPCXdndPQHaFj?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Spider-Man",
    description:
      "A young hero with superhuman strength, agility, spider-sense, and the ability to climb walls.",
    available: "N/A",
    location: "New York City",
    rank: 8,
    company: "Marvel",
    companyImageUrl:
      "https://upload.wikimedia.org/wikipedia/commons/b/b9/Marvel_Logo.svg",
    imageUrl:
      "https://tse3.mm.bing.net/th/id/OIP.H2twGsXDi-EC0A9Ej_7GhgHaHa?r=0&pid=Api&h=220&P=0",
  },

 {
    name: "Goku",
    description:
      "A Saiyan warrior who constantly pushes his limits through intense training and powerful transformations.",
    available: "Available",
    location: "Mount Paozu",
    rank: 10,
    company: "Anime",
    companyImageUrl: "https://tse2.mm.bing.net/th/id/OIP._3NgfZLYciDaj-Sm96yEHQHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl: "https://tse2.mm.bing.net/th/id/OIP.QDIxN5ir3wJ1T5Ji8SBs9QHaHa?r=0&pid=Api&h=220&P=0",
  },
  {
    name: "Iron Man",
    description:
      "A genius inventor who uses a technologically advanced armored suit to fight threats around the world.",
    available: "Available",
    location: "New York City",
    rank: 8,
    company: "Marvel",
    companyImageUrl: "https://upload.wikimedia.org/wikipedia/commons/b/b9/Marvel_Logo.svg",
    imageUrl:
      "https://tse2.mm.bing.net/th/id/OIP.tg-47q3r_StMdFwa2EeiUgAAAA?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Captain America",
    description:
      "A super-soldier with enhanced strength, speed, endurance, and exceptional combat skills.",
    available: "Available",
    location: "New York City",
    rank: 8,
    company: "Marvel",
    companyImageUrl: "https://upload.wikimedia.org/wikipedia/commons/b/b9/Marvel_Logo.svg",
    imageUrl:
      "https://tse3.mm.bing.net/th/id/OIP.JOf50pwGjDzmv-kQ4QZm-AHaHa?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Hulk",
    description:
      "A scientist whose transformation gives him immense strength, durability, and incredible physical power.",
    available: "N/A",
    location: "Unknown",
    rank: 10,
    company: "Marvel",
    companyImageUrl: "https://upload.wikimedia.org/wikipedia/commons/b/b9/Marvel_Logo.svg",
    imageUrl:
      "https://tse4.mm.bing.net/th/id/OIP.PY1URYaJ4jhs8CvbhbPKlgHaHa?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Wonder Woman",
    description:
      "An Amazon warrior princess possessing extraordinary strength, speed, durability, and combat ability.",
    available: "Available",
    location: "Themyscira",
    rank: 9,
    company: "DC",
    companyImageUrl: "https://tse2.mm.bing.net/th/id/OIP.rJkRHRfdcZDy1BGH5D0Y8AHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl:
      "https://tse3.mm.bing.net/th/id/OIP.SKO0pa8ikhXrjmCYSs98wQHaHa?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "The Flash",
    description:
      "A superhero capable of extraordinary speed through his connection to the Speed Force.",
    available: "Available",
    location: "Central City",
    rank: 9,
    company: "DC",
    companyImageUrl: "https://tse2.mm.bing.net/th/id/OIP.rJkRHRfdcZDy1BGH5D0Y8AHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl:
      "https://tse3.mm.bing.net/th/id/OIP.sxSoG4V4a-OEZT4kqqfs1QAAAA?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Aquaman",
    description:
      "The King of Atlantis with immense strength, underwater abilities, and control over marine life.",
    available: "Available",
    location: "Atlantis",
    rank: 8,
    company: "DC",
    companyImageUrl: "https://tse2.mm.bing.net/th/id/OIP.rJkRHRfdcZDy1BGH5D0Y8AHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl:
      "https://tse2.mm.bing.net/th/id/OIP.sNcZjBa-uhM90VnWUjWcyQHaHa?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Black Panther",
    description:
      "The highly skilled king of Wakanda who combines advanced technology with enhanced physical abilities.",
    available: "Available",
    location: "Wakanda",
    rank: 8,
    company: "Marvel",
    companyImageUrl: "https://upload.wikimedia.org/wikipedia/commons/b/b9/Marvel_Logo.svg",
    imageUrl:
      "https://tse3.mm.bing.net/th/id/OIP.xaFzamWv9Sx-skeC0jV9QwAAAA?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Wolverine",
    description:
      "A mutant superhero with an accelerated healing factor, enhanced senses, and retractable adamantium claws.",
    available: "N/A",
    location: "Canada",
    rank: 9,
    company: "Marvel",
    companyImageUrl: "https://upload.wikimedia.org/wikipedia/commons/b/b9/Marvel_Logo.svg",
    imageUrl:
      "https://tse3.mm.bing.net/th/id/OIP.OUrF5kZ_SbwTyeH88pgiTgHaHa?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Green Lantern",
    description:
      "A space-faring superhero who uses a power ring to create energy constructs limited by his willpower.",
    available: "Available",
    location: "Coast City",
    rank: 9,
    company: "DC",
    companyImageUrl: "https://tse2.mm.bing.net/th/id/OIP.rJkRHRfdcZDy1BGH5D0Y8AHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl:
      "https://tse2.mm.bing.net/th/id/OIP.IieFnawb9M8jXDpAi3wCrAHaHa?r=0&pid=Api&h=220&P=0",
  },

  {
    name: "Saitama",
    description:
      "The hero known as One-Punch Man, capable of defeating extremely powerful opponents with overwhelming strength.",
    available: "Available",
    location: "City Z",
    rank: 10,
    company: "Anime",
    companyImageUrl: "https://tse2.mm.bing.net/th/id/OIP._3NgfZLYciDaj-Sm96yEHQHaDt?r=0&pid=Api&h=220&P=0",
    imageUrl:
      "https://tse2.mm.bing.net/th/id/OIP.UMwM3gdNUFQBy4AQwVgCdQHaHa?r=0&pid=Api&h=220&P=0",
  }
];




  return (
    <>
    {
      heroes.map((element) => {
        return (
                  <Card name={element.name} description={element.description} available={element.available} location={element.location} rank={element.rank} company={element.company} pfp={element.imageUrl} companyURL={element.companyImageUrl}></Card>
        )
      })
    }

    </>
  )
}

export default App
