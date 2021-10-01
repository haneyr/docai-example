import os
from google.cloud import documentai_v1beta3 as documentai

project_id=  '' # Where the API is activated

location = 'us' # Format is 'us' or 'eu'
processor_id = '' # Create processor in Cloud Console
os.environ['GOOGLE_APPLLICATION_CREDENTIALS']= '/home/haneyr/key.json'
response_file = 'response.json' #outputs written here
file_path = '/home/haneyr/form.pdf' # the file you want 

def process_document(
    project_id=project_id, location=location, processor_id=processor_id,  file_path=file_path
):

    # Instantiates a client
    client = documentai.DocumentProcessorServiceClient()

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    with open(file_path, "rb") as image:
        image_content = image.read()
    
    # Read the file into memory
    document = {"content": image_content, "mime_type": "application/pdf"}

    # Configure the process request
    request = {"name": name, "document": document}

    # Use the Document AI client to process the sample form
    result = client.process_document(request=request)

    document = result.document
    document_text = document.text
    print("Document processing complete.")
    print("Text: {}".format(document_text)) 

    with open(response_file,'w') as f:
        print(document, file=f)

process_document() 
