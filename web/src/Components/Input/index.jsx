/* eslint-disable */ 
import {React, useState, useEffect, useRef} from 'react';
import axios from 'axios';
import InputStyle from './style';

function Input() {
  const [image, setImage] = useState();
  const [previewURL, setPreviewURL] = useState('');
  const [preview, setPreview] = useState(null);
  const imageRef = useRef();
  const URL = '{IP주소}/sticker/'

  useEffect(() => {
    if (image !== '')
      setPreview(
        <img className="rounded-lg drop-shadow-2xl" src={`data:image/png;base64,${previewURL}`}  alt="" />,
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


      axios.post(URL, form_data, {
        headers: {
          'content-type': 'multipart/form-data'
        },
        timeout: 50000
      }).then(res => {
          console.log(res.data.image)
          setPreviewURL(res.data.image);
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
