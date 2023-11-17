import React, { useState, useEffect } from "react";
import RideService from "../Services/RideService"


function Home() {

  const [rides, setRides] = useState([]);

  useEffect(() => {
    RideService
      .getAvailableRides()
      .then(data => {
        console.log(data)
        setRides(data)
      })
      .catch((err) => console.log(err))
  }, []);

  return (
    <div>
      <h2>Available Rides</h2>
      {/* Display a list of Rides */}
      {rides.length === 0 ? (
        <p>No Rides Available</p>
      ) : (
        <ul>
          {rides.map(ride => (
            <li key={ride.id}>
              <strong>{ride.origin}</strong> to <strong>{ride.destination}</strong>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default Home;