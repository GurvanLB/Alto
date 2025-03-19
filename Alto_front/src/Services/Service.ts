import axios from "axios";

export async function verification_jeton() {
  const token = document.cookie
    .split("; ")
    .find((row) => row.startsWith("token="))
    ?.split("=")[1];
  if (!token) {
    return false;
  }
  try {
    const reponse = await axios.post(
      "http://172.31.10.219:5000/verification_jeton",
      { Headers: { Authorization: `Bearer ${token}` } }
    );
    return reponse.data.valid;
  } catch (error) {
    console.error(error);
    return false;
  }
}

export const connecter = async (identifiant: string, mot_de_passe: string) => {
  try {
    const reponse = await axios.post(
      "http://172.31.10.219:5000/connecter",
      {
        nom: identifiant,
        mdp: mot_de_passe,
      },
      {
        withCredentials: true, // Permet d'envoyer les cookies avec la requête
      }
    );
    return reponse.data; // Si la requête est réussie, on retourne la réponse
  } catch (error: any) {
    // Même si la requête échoue (erreur HTTP comme 404 ou 401), on retourne la réponse d'erreur
    return error.response
      ? error.response.data
      : { message: "Une erreur inconnue est survenue." };
  }
};
