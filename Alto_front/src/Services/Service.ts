import { ref } from "vue";
import axios from "axios";

export const serveurDisponible = ref(true);

export const verifierServeur = async () => {
  try {
    await axios.get("http://localhost:5000/ping");
    serveurDisponible.value = true;
  } catch (error) {
    serveurDisponible.value = false;
  }
};
