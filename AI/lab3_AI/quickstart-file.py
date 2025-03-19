from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

import os
import time
from Levenshtein import distance as levenshtein_distance
from jiwer import wer  # Word Error Rate
import numpy as np
import cv2

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

# '''
# OCR: Read File using the Read API, extract text - remote
# This example will extract text in an image, then print results, line by line.
# This API call can also extract handwriting style text (not shown).
# '''
# print("===== Read File - remote =====")
# # Get an image with text
# read_image_url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
#
# # Call API with URL and raw response (allows you to get the operation location)
# read_response = computervision_client.read(read_image_url,  raw=True)
#
# # Get the operation location (URL with an ID at the end) from the response
# read_operation_location = read_response.headers["Operation-Location"]
# # Grab the ID from the URL
# operation_id = read_operation_location.split("/")[-1]
#
# # Call the "GET" API and wait for it to retrieve the results
# while True:
#     read_result = computervision_client.get_read_result(operation_id)
#     if read_result.status not in ['notStarted', 'running']:
#         break
#     time.sleep(1)
#
# # Print the detected text, line by line
# if read_result.status == OperationStatusCodes.succeeded:
#     for text_result in read_result.analyze_result.read_results:
#         for line in text_result.lines:
#             print(line.text)
#             print(line.bounding_box)
# print()
# '''
# END - Read File - remote
# '''
#
# print("End of Computer Vision quickstart.")


# TEST 1

# img = open("test2.jpeg", "rb")
# read_response = computervision_client.read_in_stream(
#     image=img,
#     mode="Printed",
#     raw=True
# )
# # print(read_response.as_dict())
#
# operation_id = read_response.headers['Operation-Location'].split('/')[-1]
# while True:
#     read_result = computervision_client.get_read_result(operation_id)
#     if read_result.status not in ['notStarted', 'running']:
#         break
#     time.sleep(1)
#
# # Print the detected text, line by line
# result = []
# if read_result.status == OperationStatusCodes.succeeded:
#     for text_result in read_result.analyze_result.read_results:
#         for line in text_result.lines:
#             print(line.text)
#             result.append(line.text)
#
# print()
#
#
# #TEST 2
# img2 = open("test1.png", "rb")
# read_response = computervision_client.read_in_stream(
#     image=img2,
#     mode="Printed",
#     raw=True
# )
# # print(read_response.as_dict())
#
# operation_id = read_response.headers['Operation-Location'].split('/')[-1]
# while True:
#     read_result = computervision_client.get_read_result(operation_id)
#     if read_result.status not in ['notStarted', 'running']:
#         break
#     time.sleep(1)
#
# # Print the detected text, line by line
# result = []
# if read_result.status == OperationStatusCodes.succeeded:
#     for text_result in read_result.analyze_result.read_results:
#         for line in text_result.lines:
#             print(line.text)
#             result.append(line.text)
#
# print()
#
# # get/define the ground truth
# groundTruth = ["Google Cloud", "Platform"]
# # groundTruth = ["Succes in rezolvarea", "tEMELOR la", "LABORAtoaree de", "Inteligenta Artificiala!"]
#
# # compute the performance
# noOfCorrectLines = sum(i == j for i, j in zip(result, groundTruth))
# print(noOfCorrectLines)

def process_image(image_path):
    """
    Procesează o imagine și returnează textul detectat.
    """

    #deschid imaginea în mod binar ("rb") și
    # o trimit către Azure Computer Vision API pentru procesare OCR
    with open(image_path, "rb") as img:
        read_response = computervision_client.read_in_stream(image=img, raw=True)

    #API-ul returnează un Operation ID,
    # pe care îl folosesc pentru a verifica progresul recunoașterii
    operation_id = read_response.headers['Operation-Location'].split('/')[-1]

    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    #lista pt text detectat
    result = []
    #lista pt bounding boxes ( zona unde s-a găsit textul )
    bounding_boxes = []

    # daca OCR a avut succes,
    # salvez textul recunoscut și bounding boxes
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                result.append(line.text)
                bounding_boxes.append(line.bounding_box)

    return result, bounding_boxes



# Evaluare calitate recunoaștere - caracter și cuvânt
def evaluate_text_recognition(extracted_text, ground_truth):
    """
    Functia evaluează calitatea recunoașterii textului:
    - la nivel de caracter (Levenshtein Distance)
    - la nivel de cuvânt (Word Error Rate)
    :param extracted_text: textul extras
    :param ground_truth: textul adevarat
    """
    # transform lista în string
    extracted_text_str = " ".join(extracted_text)
    ground_truth_str = " ".join(ground_truth)

    #distanța Levenshtein
    # (măsoară câte modificări trebuie facute pentru a transforma un text în altul)
    # Distanță mai mică (aproape de 0) → Șirurile sunt foarte asemănătoare
    #                                   (textul OCR detectat este aproape corect).
    # Distanță mare → Există multe diferențe între cele două șiruri
    #                   (textul recunoscut de OCR este departe de adevăr).
    # Dacă distanța este egală cu lungimea șirului mai lung ->
    #               înseamnă că textul OCR este complet greșit.
    char_distance = levenshtein_distance(extracted_text_str, ground_truth_str)

    #Word Error Rate (WER),
    # WER = (S+D+I)/N,
    # unde S = Numărul de cuvinte înlocuite incorect
    #      D = Numărul de cuvinte șterse (care lipsesc în textul detectat)
    #      I = Numărul de cuvinte inserate în plus
    #      N = Numărul total de cuvinte în textul corect (ground truth)
    # WER = 0% → Recunoașterea este perfectă, textul detectat este exact ca originalul
    # WER între 0% și 20% → OCR-ul este foarte precis
    # WER între 20% și 50% → Există destule erori, dar textul este lizibil
    # WER > 50% → Recunoașterea OCR este slabă și textul este foarte deformat
    # WER = 100% → Fie tot textul detectat este greșit, fie sistemul OCR nu a recunoscut nimic
    word_error = wer(ground_truth_str, extracted_text_str)


    return char_distance, word_error

# Detectare bounding boxes cu OpenCV
def detect_text_boxes(image_path):
    """
    Functia folosește procesare de imagine OpenCV pentru a detecta zonele unde se află textul.
    :param image_path: path-ul imaginii
    """

    image = cv2.imread(image_path)
    #o convertesc în grayscale pt a simplifica analiza.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplic binarizare inversată (THRESH_BINARY_INV):
    # pixelii albi devin negri și invers
    # pt a evidenția textul.
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # gasesc contururile obiectelor din imagine
    # (textul apare ca obiect distinct)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # extrag bounding boxes din contururi
    boxes = [cv2.boundingRect(cnt) for cnt in contours]
    bounding_boxes = [(x, y, x + w, y + h) for (x, y, w, h) in boxes]

    return bounding_boxes

def resize_image(image):
    # dimensiunea ecranului
    screen_width = 1366
    screen_height = 768

    # Redimensionea imaginea dacă este prea mare
    img_height, img_width = image.shape[:2]
    scale = min(screen_width / img_width, screen_height / img_height)
    new_width = int(img_width * scale)
    new_height = int(img_height * scale)
    resized_image = cv2.resize(image, (new_width, new_height))

    return new_width, new_height,resized_image


def evaluate_text_localization(image_path, extracted_boxes, ground_truth_boxes):
    """
    Funcția compară bounding boxes detectate cu bounding boxes reale (ground truth)
    și afișează imaginea la dimensiunea potrivită pentru ecran.
    """

    image = cv2.imread(image_path)

    img_height, img_width = image.shape[:2]
    new_width, new_height, resized_image = resize_image(image)

    # calculez factorii de scalare pentru
    # a adapta bounding boxes la noua dimensiune a imaginii
    scale_x = new_width / img_width
    scale_y = new_height / img_height
    resized_boxes = [(int(box[0] * scale_x), int(box[1] * scale_y), int(box[2] * scale_x), int(box[3] * scale_y))
                     for box in extracted_boxes]
    resized_ground_truth_boxes = [(int(box[0] * scale_x), int(box[1] * scale_y), int(box[4] * scale_x), int(box[5] * scale_y))
                                  for box in ground_truth_boxes]

    # desenez bounding boxes pe imaginea redimensionată
    # Verde = detectat
    for box in resized_boxes:
        cv2.rectangle(resized_image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

    #desenez bounding boxes corecte (ground truth)
    # Roșu = ground truth
    for box in resized_ground_truth_boxes:
        cv2.rectangle(resized_image, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)

    # redimensionarea ferestrei
    cv2.namedWindow("Text Localization", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Text Localization", new_width, new_height)

    # afisez imaginea și
    # astept o apăsare de tastă pentru a închide fereastra
    cv2.imshow("Text Localization", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 3. Posibilități de îmbunătățire OCR
def improve_ocr(image_path):
    """
    Funcție aplică preprocesare pe imagine pentru a crește precizia OCR.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Eroare: Imaginea nu a fost încărcată corect!")
        return []

    # Aplicare CLAHE pentru îmbunătățirea contrastului
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized = clahe.apply(image)

    # aplice filtru bilateral pentru eliminarea zgomotului fără a pierde detalii
    denoised = cv2.bilateralFilter(equalized, 9, 75, 75)

    # aplic prag Otsu
    _, otsu_threshold = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # aplic morfologie cu un kernel mic pentru a menține detaliile caracterelor
    kernel = np.ones((1, 1), np.uint8)
    processed = cv2.morphologyEx(otsu_threshold, cv2.MORPH_CLOSE, kernel)

    new_width, new_height, resized_image = resize_image(image)

    resized_original = cv2.resize(image, (new_width, new_height))
    resized_threshold = cv2.resize(processed, (new_width, new_height))

    # combin imaginile într-o singură fereastră (orizontal)
    combined = np.hstack([resized_original, resized_threshold])

    # creez și redimensionez fereastra corect
    cv2.namedWindow("Original vs. Preprocesat", cv2.WINDOW_NORMAL)
    cv2.imshow("Original vs. Preprocesat", combined)
    cv2.resizeWindow("Original vs. Preprocesat", new_width, new_height)

    # astept să se apese o tastă înainte de a închide fereastra
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # salvez imaginea temporar și aplic OCR pe ea
    processed_image_path = "processed_temp.jpg"
    cv2.imwrite(processed_image_path, resized_threshold)

    print("\nAplic OCR pe imaginea îmbunătățită")
    extracted_text, _ = process_image(processed_image_path)

    print("\nText extras după preprocesare:", extracted_text)

    return extracted_text



if __name__ == "__main__":
    image_path = "D://PycharmProjects//lab3_AI//images_lab3//1.jpg"
    ground_truth = ["În grădină, frunzele șușotesc sub pașii tăi. Măceșele roșii strălucesc în soarele blând de toamnă, iar vântul răcoros adie ușor printre crengi!"]

    print("\nAplic OCR pe imaginea originală")
    original_extracted_text, azure_boxes = process_image(image_path)
    print("\n Text extras (original):", original_extracted_text)

    # evaluare calitate recunoaștere (Original)
    print("\nEvaluare OCR - Imagine Originală:")
    char_distance, word_error = evaluate_text_recognition(original_extracted_text, ground_truth)
    print(f"Distanță Levenshtein (Caracter): {char_distance}")
    print(f"Word Error Rate (Cuvânt): {word_error:.2%}")


    # detectare și comparare bounding boxes
    opencv_boxes = detect_text_boxes(image_path)
    evaluate_text_localization(image_path, opencv_boxes, azure_boxes)

    # imbunătățire OCR prin procesare
    print("\nÎmbunătățire imagine pentru OCR...")
    improved_extracted_text = improve_ocr(image_path)

    # evaluare calitate recunoaștere (după preprocesare)
    print("\nEvaluare OCR - Imagine imbunătățită:")
    char_distance_improved, word_error_improved = evaluate_text_recognition(improved_extracted_text, ground_truth)
    print(f"Distanță Levenshtein (Caracter): {char_distance_improved}")
    print(f"Word Error Rate (Cuvânt): {word_error_improved:.2%}")
