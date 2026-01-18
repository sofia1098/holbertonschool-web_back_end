import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  const listaDeTareas = [uploadPhoto(), createUser()];

  return Promise.all(listaDeTareas)
    .then((respuestas) => {
      const foto = respuestas[0];
      const usuario = respuestas[1];
      console.log(`${foto.body} ${usuario.firstName} ${usuario.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
