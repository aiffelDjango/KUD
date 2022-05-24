/* eslint-disable */ 
import {React, useState, useEffect, useRef} from 'react';
import axios from 'axios';
import InputStyle from './style';

function Input() {
  const [image, setImage] = useState();
  const [previewURL, setPreviewURL] = useState('');
  const [preview, setPreview] = useState(null);
  const imageRef = useRef();
  const URL = 'http://localhost:8000/sticker/'

  useEffect(() => {
    if (image !== '')
      setPreview(
        <img className="rounded-lg drop-shadow-2xl" src={previewURL} alt="" />,
      );
    return () => {};
  }, [previewURL]);

  const imageOnChange = e => {
    e.preventDefault();
    const getImage = e.target.files[0];
    const reader = new FileReader();
    let form_data = new FormData();
      console.log(image)

      form_data.append('image', getImage);

      let url = 'http://localhost:8000/sticker/';

      axios.post(url, form_data, {
        headers: {
          'content-type': 'multipart/form-data'
        }
      }).then(res => {
          console.log(res.data);
        }).catch(err => console.log(err)) 

    reader.onloadend = () => {
      setImage(() => getImage);
    };

  };
  const imageOnClick = e => {
    e.preventDefault();
    imageRef.current.click();
  };

  return (
    <InputStyle
      preview={preview}
      onChange={imageOnChange}
      onClick={imageOnClick}
      imageRef={imageRef}
    />
  );
}

export default Input;
