const RIDES_ENDPOINT = 'http://localhost:8080/rides';

class RideService {
  async getAvailableRides() {
    try {
      const response = await fetch(RIDES_ENDPOINT);
      const data = await response.json();
      return data;
    } catch (error) {
      console.log(`Error fetching rides: ${error}`);
      throw error;
    }
  };
};

export default new RideService();
