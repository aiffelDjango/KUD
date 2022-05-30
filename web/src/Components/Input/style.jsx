import {React} from 'react';

function InputStyle({preview, imageRef, onChange, onClick}) {
  return (
    <div>
      <div className="flex justify-center mt-8">
        <div className="max-w-2xl rounded-lg shadow-xl bg-gray-50">
          <div className="m-4">
            <div
              className="inline-block mb-2 text-gray-500 w-full text-center"
              htmlFor="imageInput"
            >
              File Upload
            </div>
            <div className="flex items-center justify-center w-full pointer-events-none">
              <div className="flex flex-col w-full h-32 border-4 border-blue-200 border-dashed hover:bg-gray-100 hover:border-gray-300">
                <div className="flex flex-col items-center justify-center pt-7">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="w-8 h-8 text-gray-400 group-hover:text-gray-600"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                    />
                  </svg>
                  <p className="pt-1 text-sm tracking-wider text-gray-400 group-hover:text-gray-600 pointer-events-none">
                    Attach a file
                  </p>
                </div>
                <input
                  ref={imageRef}
                  onChange={onChange}
                  type="file"
                  className="opacity-0"
                />
              </div>
            </div>
          </div>
          <div className="flex justify-center p-2">
            <button
              type="button"
              onClick={onClick}
              className="w-full px-4 py-2 text-white bg-blue-500 rounded shadow-xl"
            >
              Upload
            </button>
          </div>
        </div>
      </div>
      <div className="w-full">
        <div className="w-4/12 rounded-lg mx-auto mt-16 p-2 bg-white">
          {preview}
        </div>
      </div>
    </div>
  );
}

export default InputStyle;
