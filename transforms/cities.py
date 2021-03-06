{
    'sheet': 'City Differences_v3',
    'lets': {
        'iri': 'vm:issues/{row[Stakeholder].as_slug}/{row[Title].as_slug}',
        'stakeholderName': '{row[Stakeholder]}',
    },
    'queries': {
        'stakeholder': (
            'select ?s where {'
            ' ?s rdf:type vm:Stakeholder .'
            ' ?s vm:name ?stakeholderName .'
            '}'),
    },
    'triples': [
        ('{iri}', 'rdf:type', 'vm:Issue'),
        ('{iri}', 'vm:name', '{row[Title]}'),
        ('{iri}', 'vm:description', '{row[Text]}'),
        ('{iri}', 'vm:ofStakeholder', '{stakeholder}'),
        ('{iri}', 'vm:atGeoPoint', '{row[Coordinates].as_geo}'),
        ('{iri}', 'vm:hasIcon', '{row[Icon]}'),
        ('{iri}', 'vm:hasAspect', '{row[Text Position].as_slug}'),
        ('{iri}', 'vm:ofStory', 'vm:stories/3'),
    ],
}
