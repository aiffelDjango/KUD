import {React, useState, useEffect, useRef} from 'react';
import InputStyle from './style';

function Input() {
  const [image, setImage] = useState();
  const [previewURL, setPreviewURL] = useState('');
  const [preview, setPreview] = useState(null);
  const imageRef = useRef();

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

    reader.onloadend = () => {
      setImage(getImage);
      setPreviewURL(reader.result);
    };
    if (getImage) reader.readAsDataURL(getImage);
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
